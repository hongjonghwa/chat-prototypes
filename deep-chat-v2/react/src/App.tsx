import { useState } from 'react'
import { DeepChat } from 'deep-chat-react';
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [stream, setStream] = useState(true)
  const history = [
    { role: 'user', text: 'Hey, how are you today?' },
    { role: 'ai', text: 'I am doing very well!' },
    { role: 'humam', text: 'Hey, how are you today?' },
    { role: 'system', text: 'I am doing very well!' },
    { role: 'user', text: 'Hey, how are you today?' },
    { role: 'ai', text: 'I am doing very well!' },
  ]
  const connect = {
    // url: "http://127.0.0.1:8080/chat-stream",
    url: "http://127.0.0.1:8080/chat",
    method: "POST",
    // stream: true,
    stream: false,
    headers: {"customName": "customHeaderValue"},
    additionalBodyProps: {"customBodyField": "customBodyValue"}
  }

  return (
    <>
      <div>
        <h1>Test Chat</h1>
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <button onClick={() => setStream((stream) => !stream)}>
        stream is {stream ? 'on' : 'off'}
        </button>
        <DeepChat
          demo={true}
          connect={connect}
          onMessage={(message) => console.log(message)}
          style={{ borderRadius:  '10px', backgroundColor: '#292929',width: '75vw', height: 'calc(100vh - 70px)', paddingTop: '10px' }}
          messageStyles={{
            default: {
              ai: {bubble: {backgroundColor: "#545454", color: "white"}}
            },
            loading: {
              message:{
                styles:{bubble: {backgroundColor: "#545454", color: "white"}}
              }
            }
          }}
          textInput={{ 
            styles: {
              container: {
                width: "100%",
                margin: "0",
                border: "unset",
                borderTop: "1px solid #d5d5d5",
                borderRadius: "0px",
                boxShadow: "unset"
              },
              text: {
                fontSize: "1.05em",
                paddingTop: "11px",
                paddingBottom: "13px",
                paddingLeft: "12px",
                paddingRight: "2.4em"
              }
            },
            placeholder: { text: 'Welcome to the demo!' , style: {color: "#bcbcbc"}} 
          }}
          submitButtonStyles={{
            "submit": {
              "container": {
                "default": {
                  "transform": "scale(1.21)",
                  "marginBottom": "-3px",
                  "marginRight": "0.4em"
                }
              }
            }
          }}
          history={history}
        />
        
      </div>

    </>
  )
}

export default App
