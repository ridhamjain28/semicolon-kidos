const BASE_URL = "http://localhost:8000";

export const api = {
  async fetchContent(topic: string, age: number) {
    const res = await fetch(`${BASE_URL}/cognicards/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic, age })
    });
    return res.json();
  },

  async logSignal(userId: string, signalType: string, value: number) {
    return fetch(`${BASE_URL}/iblm/signal`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: userId,
        signal_type: signalType,
        value: value,
        event_type: "interaction"
      })
    });
  }
};
