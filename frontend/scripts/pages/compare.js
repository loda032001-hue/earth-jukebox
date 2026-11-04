const API_BASE = window.EJ_API_BASE || "http://127.0.0.1:8000";

document.getElementById("run").addEventListener("click", async () => {
  const p = (id) => document.getElementById(id).value;
  const url = `${API_BASE}/api/compare?lat1=${p("lat1")}&lon1=${p("lon1")}&start1=${p("start1")}&end1=${p("end1")}&lat2=${p("lat2")}&lon2=${p("lon2")}&start2=${p("start2")}&end2=${p("end2")}&parameter=${p("param")}`;
  try {
    const res = await fetch(url);
    const data = await res.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    document.getElementById("result").textContent = "Error: " + e.message;
  }
});
