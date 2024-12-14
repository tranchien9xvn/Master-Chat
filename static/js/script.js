// Script để xử lý gửi tin nhắn
document.addEventListener("DOMContentLoaded", () => {
    const inputField = document.querySelector(".chat-input input");
    const sendButton = document.querySelector(".chat-input button");
    const messagesContainer = document.querySelector(".chat-messages");
  
    // Hàm thêm tin nhắn vào giao diện
    function addMessage(content, type = "sent") {
      const messageElement = document.createElement("div");
      messageElement.classList.add("message", type);
      messageElement.textContent = content;
      messagesContainer.appendChild(messageElement);
  
      // Cuộn xuống cuối cùng
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
  
    // Xử lý khi bấm nút gửi
    sendButton.addEventListener("click", () => {
      const message = inputField.value.trim();
      if (message) {
        addMessage(message, "sent"); // Thêm tin nhắn người dùng
        inputField.value = ""; // Xoá input sau khi gửi
        simulateReply(); // Gọi hàm trả lời tự động
      }
    });
  
    // Xử lý khi nhấn Enter
    inputField.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        sendButton.click(); // Gửi tin nhắn
      }
    });
  
    // Hàm mô phỏng trả lời tự động
    function simulateReply() {
      setTimeout(() => {
        const replies = [
          "Xin chào! 😊",
          "Tôi có thể giúp gì cho bạn?",
          "Thật tuyệt khi nói chuyện với bạn!",
          "Cảm ơn bạn đã liên hệ.",
        ];
        const randomReply = replies[Math.floor(Math.random() * replies.length)];
        addMessage(randomReply, "received");
      }, 1000); // Trả lời sau 1 giây
    }
  });
  