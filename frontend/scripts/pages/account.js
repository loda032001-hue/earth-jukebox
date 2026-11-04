const API_BASE = window.EJ_API_BASE || "http://127.0.0.1:8000";

async function post(path, body) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

document.getElementById("signup").addEventListener("click", async () => {
  try {
    const data = await post("/api/auth/signup", {
      email: document.getElementById("su-email").value,
      password: document.getElementById("su-pass").value,
    });
    localStorage.setItem("ej-token", data.access_token);
    localStorage.setItem("ej-user", data.user_id);
    alert("Registrado");
  } catch (e) {
    alert("Error: " + e.message);
  }
});

document.getElementById("login").addEventListener("click", async () => {
  try {
    const data = await post("/api/auth/login", {
      email: document.getElementById("li-email").value,
      password: document.getElementById("li-pass").value,
    });
    localStorage.setItem("ej-token", data.access_token);
    localStorage.setItem("ej-user", data.user_id);
    alert("Sesión iniciada");
  } catch (e) {
    alert("Error: " + e.message);
  }
});

document.getElementById("me").addEventListener("click", async () => {
  const token = localStorage.getItem("ej-token");
  if (!token) {
    document.getElementById("profile").textContent = "No hay sesión";
    return;
  }
  try {
    const res = await fetch(`${API_BASE}/api/auth/me?token=${encodeURIComponent(token)}`);
    const data = await res.json();
    document.getElementById("profile").textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    document.getElementById("profile").textContent = "Error: " + e.message;
  }
});
