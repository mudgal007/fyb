import React, { createContext, useContext, useEffect, useMemo, useRef, useState } from 'react';

const RealtimeContext = createContext();

export function RealtimeProvider({ children }) {
  const socketRef = useRef(null);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const socket = new WebSocket(`ws://${window.location.hostname}:8000/ws/activity`);
    socketRef.current = socket;

    socket.addEventListener('message', (event) => {
      try {
        const data = JSON.parse(event.data);
        setEvents((prev) => [...prev.slice(-10), data]);
      } catch (error) {
        console.error('Realtime parse error', error);
      }
    });

    return () => socket.close();
  }, []);

  const value = useMemo(
    () => ({
      events,
      send: (payload) => {
        if (socketRef.current?.readyState === WebSocket.OPEN) {
          socketRef.current.send(JSON.stringify(payload));
        }
      }
    }),
    [events]
  );

  return <RealtimeContext.Provider value={value}>{children}</RealtimeContext.Provider>;
}

export function useRealtime() {
  const context = useContext(RealtimeContext);
  if (!context) {
    throw new Error('useRealtime must be used within a RealtimeProvider');
  }
  return context;
}
