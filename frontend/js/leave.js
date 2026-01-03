const BASE_URL = "http://127.0.0.1:5000";

async function applyLeave() {
  const token = localStorage.getItem("token");

  const payload = {
    leave_type_id: document.getElementById("leave_type_id").value,
    start_date: document.getElementById("start_date").value,
    end_date: document.getElementById("end_date").value,
    reason: document.getElementById("reason").value
  };

  const response = await fetch(`${BASE_URL}/leave/apply`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": token
    },
    body: JSON.stringify(payload)
  });

  const data = await response.json();
  alert(data.message);
}
