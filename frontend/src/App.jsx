import { useState } from 'react'
import axios from 'axios' // The Messenger
import { Send, Bot, User } from 'lucide-react'

function App() {
  const [message, setMessage] = useState("")
  const [chatHistory, setChatHistory] = useState([]) // Memory of the conversation
  const [isLoading, setIsLoading] = useState(false)

  const handleSend = async () => {
    if (!message) return;

    // 1. Add YOUR message to the screen immediately
    const userMessage = { role: "user", text: message }
    setChatHistory(prev => [...prev, userMessage])
    setIsLoading(true)

    try {
      // 2. Prepare the data (The Backend expects 'FormData')
      const formData = new FormData()
      formData.append("text_prompt", message)

      // 3. Send it to Python (The Waiter runs to the kitchen)
      const response = await axios.post("http://127.0.0.1:8000/chat", formData)

      // 4. Add the AI's response to the screen
      const aiMessage = { role: "ai", text: response.data.Response }
      setChatHistory(prev => [...prev, aiMessage])

    } catch (error) {
      console.error("Error talking to backend:", error)
      const errorMessage = { role: "ai", text: "❌ Error: Is the backend server running?" }
      setChatHistory(prev => [...prev, errorMessage])
    }

    setIsLoading(false)
    setMessage("") // Clear the input box
  }

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "20px", fontFamily: "sans-serif" }}>
      <h1>🤖 AI Pair Programmer</h1>

      {/* CHAT DISPLAY AREA */}
      <div style={{ 
        border: "1px solid #ccc", 
        borderRadius: "10px", 
        height: "400px", 
        overflowY: "scroll", 
        padding: "10px",
        marginBottom: "20px",
        display: "flex",
        flexDirection: "column",
        gap: "10px"
      }}>
        {chatHistory.map((msg, index) => (
          <div key={index} style={{ 
            display: "flex", 
            alignItems: "center",
            gap: "10px",
            alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
            backgroundColor: msg.role === "user" ? "#007bff" : "#f1f1f1",
            color: msg.role === "user" ? "white" : "black",
            padding: "10px",
            borderRadius: "10px",
            maxWidth: "70%"
          }}>
            {msg.role === "ai" && <Bot size={20} />}
            <span>{msg.text}</span>
            {msg.role === "user" && <User size={20} />}
          </div>
        ))}
        
        {isLoading && <p style={{fontStyle: "italic", color: "gray"}}>Thinking...</p>}
      </div>

      {/* INPUT AREA */}
      <div style={{ display: "flex", gap: "10px" }}>
        <input 
          type="text"
          placeholder="Ask me to write code..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          style={{ flex: 1, padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
        />
        <button 
          onClick={handleSend}
          disabled={isLoading}
          style={{ 
            padding: "10px 20px", 
            cursor: "pointer", 
            backgroundColor: isLoading ? "#ccc" : "green",
            color: "white",
            border: "none",
            borderRadius: "5px",
            display: "flex",
            alignItems: "center",
            gap: "5px"
          }}
        >
          <Send size={18} />
          {isLoading ? "..." : "Send"}
        </button>
      </div>
    </div>
  )
}

export default App