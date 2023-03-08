document.addEventListener("DOMContentLoaded", () => {
  const inputField = document.getElementById("input");
  inputField.addEventListener("keydown", (e) => {
    if (e.code === "Enter") {
      let input = inputField.value;
      inputField.value = "";
      output(input);
    }
  });
});

function output(input) {
  let url = "/glam";

  fetch(url, {
    method: "POST",
    body: JSON.stringify({ input: input }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => createChatBubble(data));
}

function createChatBubble(val) {
  console.log(val);
  const bubble = document.createElement("div");
  bubble.setAttribute("class", "bubble");

  const text = document.createElement("span");
  text.setAttribute("class", "chat-text");
  text.innerText = val.message;

  bubble.appendChild(text);

  const chat = document.getElementById("chat");
  chat.appendChild(bubble);
}
