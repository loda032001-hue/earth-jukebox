"""Catálogo de sonidos naturales (Etapa 3).

Los registros iniciales provienen de Wikimedia Commons y se incluyen con
metadatos verificables. No se inventan ubicaciones: cuando no hay coordenadas,
location_precision se marca como "unconfirmed"/"region" y no se generan
marcadores en el mapa.
"""

from app.schemas.sound import NaturalSound, SoundCategory

CATEGORIES: list[SoundCategory] = [
    SoundCategory(slug="volcanoes", name="Volcanes", description="Actividad volcánica."),
    SoundCategory(slug="storms", name="Tormentas", description="Fenómenos tormentosos."),
    SoundCategory(slug="oceans", name="Océanos", description="Sonidos del mar."),
    SoundCategory(slug="waterfalls", name="Cascadas", description="Cascadas y saltos de agua."),
    SoundCategory(slug="rivers", name="Ríos", description="Cursos de agua."),
    SoundCategory(slug="glaciers", name="Glaciares", description="Masas de hielo glaciar."),
    SoundCategory(slug="ice", name="Hielo", description="Hielo y nieve."),
    SoundCategory(slug="wind", name="Viento", description="Viento y brisa."),
    SoundCategory(slug="rain", name="Lluvia", description="Lluvia y precipitación."),
    SoundCategory(slug="fauna", name="Fauna", description="Vida silvestre."),
    SoundCategory(slug="forests", name="Bosques", description="Ambientes forestales."),
    SoundCategory(slug="geology", name="Actividad geológica", description="Fenómenos geológicos."),
    SoundCategory(slug="other", name="Otros", description="Otros fenómenos naturales."),
]

SEED_SOUNDS: list[NaturalSound] = [
    NaturalSound(
        id="9e389661-227e-42e4-9261-145f83d7c9a1",
        name="Trueno 01",
        category="storms",
        description="Grabación de trueno publicada en Wikimedia Commons.",
        image_url="https://thumb.wikimedia.org/wikipedia/commons/thumb/0/07/ISS-20_Thunderstorms_on_the_Brazilian_Horizon.jpg/500px-ISS-20_Thunderstorms_on_the_Brazilian_Horizon.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail",
        audio_url="https://upload.wikimedia.org/wikipedia/commons/f/fa/Thunder_01.ogg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original",
        duration_seconds=9,
        recorded_at="2023-04-30",
        author="Amuzujoe",
        source="Wikimedia Commons",
        license="CC BY-SA 4.0",
        scientific_info="Fenómeno atmosférico: descarga eléctrica en tormenta.",
        tags=["trueno", "tormenta"],
        location_precision="unconfirmed",
        coordinate_source="none",
    ),
    NaturalSound(
        id="f524120f-9d12-4287-8a5a-a16ec4d43542",
        name="Sonido de lluvia",
        category="rain",
        description="Grabación de lluvia publicada en Wikimedia Commons.",
        image_url="https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9d/Rain_drops_vehicle_mirror_window_06.jpg/500px-Rain_drops_vehicle_mirror_window_06.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail",
        audio_url="https://upload.wikimedia.org/wikipedia/commons/8/8a/Sound_of_rain.ogg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original",
        duration_seconds=26,
        recorded_at="2014-05-12",
        author="Effib",
        source="Wikimedia Commons",
        license="CC BY-SA 3.0",
        scientific_info="Precipitación líquida; intensidad variable.",
        tags=["lluvia", "precipitación"],
        location_precision="unconfirmed",
        coordinate_source="none",
    ),
    NaturalSound(
        id="5b46ebdc-2c3f-49d4-a577-be227c260147",
        name="Olas del océano rompiendo",
        category="oceans",
        description="Grabación de campo de olas rompiendo en la orilla (Kalundborg Fjord, Røsnæs).",
        image_url="https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ef/Waves_crashing_against_the_Santa_Cruz_Shore_%284788703579%29.jpg/500px-Waves_crashing_against_the_Santa_Cruz_Shore_%284788703579%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail",
        audio_url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Oceanwavescrushing.ogg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original",
        duration_seconds=120,
        recorded_at="2008-02-16",
        author="Luftrum (vía Freesound)",
        source="Wikimedia Commons (originally Freesound)",
        license="CC BY 3.0",
        country="Dinamarca",
        region="Fiordo de Kalundborg, Røsnæs",
        continent="Europa",
        ecosystem="costa",
        scientific_info="Oleaje y rompiente en zona costera.",
        tags=["olas", "océano", "costa"],
        location_precision="region",
        coordinate_source="place name in description (no exact coordinates)",
    ),
    NaturalSound(
        id="0a6d3e8a-e4e3-45fc-893d-6d905a7648a2",
        name="Coro del amanecer (East/West Sussex, UK)",
        category="fauna",
        description="Grabación de campo del coro del amanecer en un pequeño bosque, una hora antes del amanecer.",
        audio_url="https://upload.wikimedia.org/wikipedia/commons/8/84/0426AM_Dawn_Chorus_07-May-2023.ogg",
        duration_seconds=4052,
        country="Reino Unido",
        region="East/West Sussex",
        continent="Europa",
        ecosystem="bosque",
        latitude=51.1225,
        longitude=-0.016667,
        location_precision="approximate",
        coordinate_source="GPS en descripción de Wikimedia Commons (aproximado)",
        recorded_at="2023-05-07",
        author="Alexander Wendt",
        source="Wikimedia Commons",
        license="CC BY-SA 4.0",
        scientific_info="Coro de aves al amanecer; densidad y variedad de especies.",
        tags=["aves", "amanecer", "bosque"],
    ),
    NaturalSound(
        id="44028e3a-b9e2-467c-9da8-f7415a5f331d",
        name="Ranas cantando (Presqu'ile, Canadá)",
        category="fauna",
        description="Grabación de campo de ranas (Pseudacris crucifer y Lithobates sylvaticus) en un estanque.",
        audio_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Pseudacris-crucifer-003.ogg",
        duration_seconds=120,
        country="Canadá",
        region="Ontario, Presqu'ile Provincial Park",
        continent="América del Norte",
        ecosystem="humedal",
        latitude=43.99389,
        longitude=-77.71306,
        location_precision="approximate",
        coordinate_source="Coordenadas de Wikipedia para Presqu'ile Provincial Park (nivel de parque, no sitio exacto)",
        recorded_at="2006-04-16",
        author="Mdf",
        source="Wikimedia Commons",
        license="CC BY-SA 3.0",
        scientific_info="Vocalización de anfibios; indicador de salud del humedal.",
        tags=["ranas", "anfibios", "humedal"],
    ),
    NaturalSound(
        id="5a3d0a00-7271-42a8-8b6f-5a491f64d816",
        name="Mercado de Idumota (Lagos, Nigeria)",
        category="other",
        description="Paisaje sonoro del mercado de Idumota en Lagos.",
        audio_url="https://upload.wikimedia.org/wikipedia/commons/a/a8/Idumota_Market_%28Emeka_Ogboh%29.ogg",
        duration_seconds=300,
        country="Nigeria",
        region="Lagos",
        continent="África",
        ecosystem="urbano",
        latitude=6.5244,
        longitude=3.3792,
        location_precision="approximate",
        coordinate_source="Coordenadas a nivel de ciudad para Lagos, Nigeria (Wikipedia)",
        recorded_at="2009-05-01",
        author="Emeka Ogboh",
        source="Wikimedia Commons",
        license="CC BY-SA 3.0",
        scientific_info="Paisaje sonoro urbano; diversidad acústica.",
        tags=["mercado", "urbano", "Lagos"],
    ),
]


def list_categories() -> list[SoundCategory]:
    return CATEGORIES


def list_sounds(category: str | None = None, query: str | None = None, limit: int | None = None, offset: int = 0) -> list[NaturalSound]:
    items = SEED_SOUNDS
    if category:
        items = [s for s in items if s.category == category]
    if query:
        q = query.lower()
        items = [s for s in items if q in s.name.lower() or q in (s.description or "").lower() or any(q in t for t in s.tags)]
    if offset:
        items = items[offset:]
    if limit is not None:
        items = items[:limit]
    return items


def get_sound(sound_id: str) -> NaturalSound | None:
    for s in SEED_SOUNDS:
        if s.id == sound_id:
            return s
    return None


def geolocated_sounds() -> list[NaturalSound]:
    """Solo sonidos con coordenadas verificables."""
    return [s for s in SEED_SOUNDS if s.latitude is not None and s.longitude is not None]
