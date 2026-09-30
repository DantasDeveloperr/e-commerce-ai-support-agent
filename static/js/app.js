const chatToggle = document.getElementById("chat-toggle");
const chatClose = document.getElementById("chat-close");

const chatContainer = document.getElementById("chat-container");

const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

const chatMessages = document.getElementById("chat-messages");


// Abrir o chat

chatToggle.addEventListener("click", () => {
    chatContainer.style.display = "flex";
    messageInput.focus();
});


// Fechar o chat

chatClose.addEventListener("click", () => {
    chatContainer.style.display = "none";
});


// Adicionar mensagem na interface

function addMessage(message, type) {
    const messageElement = document.createElement("div");

    messageElement.classList.add("message");

    if (type === "user") {
        messageElement.classList.add("user-message");
    } else {
        messageElement.classList.add("bot-message");
    }

    messageElement.textContent = message;

    chatMessages.appendChild(messageElement);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}


// Mostrar indicador de carregamento

// Mostrar indicador de carregamento

function showTypingIndicator() {
    const typingElement = document.createElement("div");

    typingElement.id = "typing-indicator";
    typingElement.classList.add(
        "message",
        "bot-message",
        "typing-indicator"
    );

    for (let i = 0; i < 3; i++) {
        const dot = document.createElement("span");

        dot.classList.add("typing-dot");

        typingElement.appendChild(dot);
    }

    chatMessages.appendChild(typingElement);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Remover indicador de carregamento

function removeTypingIndicator() {
    const typingElement = document.getElementById("typing-indicator");

    if (typingElement) {
        typingElement.remove();
    }
}


// Alterar estado do botão

function setLoadingState(isLoading) {
    sendButton.disabled = isLoading;
    messageInput.disabled = isLoading;

    if (isLoading) {
        sendButton.textContent = "Enviando...";
    } else {
        sendButton.textContent = "Enviar";
    }
}


// Enviar mensagem

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");

    messageInput.value = "";

    setLoadingState(true);
    showTypingIndicator();

    try {
        const response = await fetch("/chat", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error("Erro ao comunicar com a API.");
        }

        const data = await response.json();

        removeTypingIndicator();

        addMessage(data.response, "bot");

    } catch (error) {
        console.error(error);

        removeTypingIndicator();

        addMessage(
            "Desculpe, ocorreu um erro ao tentar falar com o servidor.",
            "bot"
        );

    } finally {
        setLoadingState(false);
        messageInput.focus();
    }
});