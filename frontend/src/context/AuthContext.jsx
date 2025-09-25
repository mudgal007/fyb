import React, { createContext, useCallback, useContext, useMemo, useState } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setToken] = useState(null);
  const [profile, setProfile] = useState(null);

  const login = useCallback((nextToken, userProfile) => {
    setToken(nextToken);
    setProfile(userProfile);
  }, []);

  const logout = useCallback(() => {
    setToken(null);
    setProfile(null);
  }, []);

  const value = useMemo(
    () => ({
      token,
      profile,
      isAuthenticated: Boolean(token),
      login,
      logout
    }),
    [token, profile, login, logout]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
