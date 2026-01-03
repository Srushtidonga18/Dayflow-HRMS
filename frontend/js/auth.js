const BASE_URL = "http://127.0.0.1:5000";

/* ---------------- LOGIN ---------------- */
async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch(`${BASE_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email, password })
    });

    const data = await response.json();

    if (!response.ok) {
      alert(data.message || "Login failed");
      return;
    }

    // ✅ STORE AUTH DATA
    localStorage.setItem("token", data.token);
    localStorage.setItem("role", data.role);

    // ✅ STORE REAL USER OBJECT FROM BACKEND
    localStorage.setItem("user", JSON.stringify(data.user));

    alert("Login successful ✅");
    window.location.href = "employee_dashboard.html";

  } catch (error) {
    console.error("Login error:", error);
    alert("Server error during login");
  }
}

/* ---------------- SIGNUP ---------------- */
async function signup() {
  const payload = {
    first_name: document.getElementById("firstName").value,
    last_name: document.getElementById("lastName").value,
    employee_id: document.getElementById("employeeId").value,
    company_code: document.getElementById("companyCode").value,
    email: document.getElementById("email").value,
    password: document.getElementById("password").value,
    role: document.getElementById("role").value,
    year_of_joining: document.getElementById("yearOfJoining").value
  };

  try {
    const response = await fetch(`${BASE_URL}/auth/signup`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    alert(data.message);

    if (response.ok) {
      window.location.href = "login.html";
    }

  } catch (error) {
    console.error("Signup error:", error);
    alert("Server error during signup");
  }
}

/* ---------------- LOGOUT ---------------- */
function logout() {
  localStorage.clear();
  window.location.href = "login.html";
}
