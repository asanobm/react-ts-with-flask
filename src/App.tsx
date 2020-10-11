import React, { useState, useEffect } from 'react'

interface Hello {
  message: string
}

const App: React.FC = () => {
  const [hello, setHello] = useState<Hello>()

  useEffect(() => {
    const getHello = async () => {
      await fetch('/api/hello')
        .then((res) => res.json())
        .then((data: Hello) => setHello(data))
    }
    getHello()
  }, [])
  return (
    <div>
      <h1>hello</h1>
      <span>{hello?.message}</span>
    </div>
  )
}

export default App
