// Motor de audio del laboratorio (Web Audio API) — Etapa 5.
export class AudioEngine {
  constructor() {
    this.ctx = null;
    this.masterGain = null;
    this.analyser = null;
    this.layers = new Map();
    this.playing = false;
    this.masterVolume = 0.7;
  }

  ensureContext() {
    if (!this.ctx) {
      this.ctx = new (window.AudioContext || window.webkitAudioContext)();
      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.value = this.masterVolume;
      this.analyser = this.ctx.createAnalyser();
      this.analyser.fftSize = 64;
      this.masterGain.connect(this.analyser);
      this.analyser.connect(this.ctx.destination);
    }
    if (this.ctx.state === "suspended") this.ctx.resume();
  }

  // Generador de ruido blanco
  createNoiseBuffer() {
    const buffer = this.ctx.createBuffer(1, this.ctx.sampleRate * 2, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < data.length; i++) data[i] = Math.random() * 2 - 1;
    return buffer;
  }

  addLayer(id, config) {
    this.layers.set(id, {
      id,
      name: config.name,
      type: config.type,
      baseFreq: config.baseFreq || 220,
      volume: config.volume ?? 0.5,
      enabled: config.enabled ?? false,
      nodes: null,
    });
  }

  buildLayer(layer) {
    this.ensureContext();
    const gain = this.ctx.createGain();
    gain.gain.value = layer.enabled ? layer.volume : 0;
    let source;
    if (layer.type === "noise") {
      source = this.ctx.createBufferSource();
      source.buffer = this.createNoiseBuffer();
      source.loop = true;
      const filter = this.ctx.createBiquadFilter();
      filter.type = "lowpass";
      filter.frequency.value = layer.baseFreq;
      source.connect(filter);
      filter.connect(gain);
    } else {
      source = this.ctx.createOscillator();
      source.type = layer.type;
      source.frequency.value = layer.baseFreq;
      source.connect(gain);
    }
    gain.connect(this.masterGain);
    layer.nodes = { source, gain };
    return layer;
  }

  setLayerEnabled(id, enabled) {
    const layer = this.layers.get(id);
    if (!layer) return;
    layer.enabled = enabled;
    if (layer.nodes) {
      layer.nodes.gain.gain.setTargetAtTime(enabled ? layer.volume : 0, this.ctx.currentTime, 0.05);
    }
  }

  setLayerVolume(id, value) {
    const layer = this.layers.get(id);
    if (!layer) return;
    layer.volume = value;
    if (layer.nodes && layer.enabled) {
      layer.nodes.gain.gain.setTargetAtTime(value, this.ctx.currentTime, 0.05);
    }
  }

  setLayerBaseFreq(id, freq) {
    const layer = this.layers.get(id);
    if (!layer) return;
    layer.baseFreq = freq;
    if (layer.nodes && layer.nodes.source.frequency) {
      layer.nodes.source.frequency.setTargetAtTime(freq, this.ctx.currentTime, 0.05);
    }
  }

  play() {
    this.ensureContext();
    this.layers.forEach((layer) => {
      if (!layer.nodes) this.buildLayer(layer);
      try { layer.nodes.source.start(); } catch (e) { /* already started */ }
      layer.nodes.gain.gain.setTargetAtTime(layer.enabled ? layer.volume : 0, this.ctx.currentTime, 0.05);
    });
    this.playing = true;
  }

  pause() {
    if (!this.ctx) return;
    this.ctx.suspend();
    this.playing = false;
  }

  resume() {
    if (!this.ctx) return;
    this.ctx.resume();
    this.playing = true;
  }

  stop() {
    if (!this.ctx) return;
    this.layers.forEach((layer) => {
      if (layer.nodes) {
        try { layer.nodes.source.stop(); } catch (e) {}
        layer.nodes = null;
      }
    });
    this.playing = false;
  }

  setMasterVolume(value) {
    this.masterVolume = value;
    if (this.masterGain) this.masterGain.gain.setTargetAtTime(value, this.ctx.currentTime, 0.05);
  }

  getAnalyser() {
    return this.analyser;
  }

  saveComposition(name) {
    const state = {
      name,
      masterVolume: this.masterVolume,
      layers: Array.from(this.layers.values()).map((l) => ({
        id: l.id,
        enabled: l.enabled,
        volume: l.volume,
      })),
    };
    const all = JSON.parse(localStorage.getItem("ej-compositions") || "[]");
    all.push(state);
    localStorage.setItem("ej-compositions", JSON.stringify(all));
    return state;
  }

  loadCompositions() {
    return JSON.parse(localStorage.getItem("ej-compositions") || "[]");
  }
}
