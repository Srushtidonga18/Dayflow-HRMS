const BASE_URL = "http://127.0.0.1:5000";

async function checkIn() {
  const token = localStorage.getItem("token");

  const response = await fetch(`${BASE_URL}/attendance/checkin`, {
    method: "POST",
    headers: {
      "Authorization": token
    }
  });

  const data = await response.json();
  alert(data.message);
}
