import { createContext, useContext, useEffect, useState, type ReactNode } from "react";

type Mode = "light" | "dark";
interface ThemeCtx {
  mode: Mode;
  toggle: () => void;
}

const Ctx = createContext<ThemeCtx | null>(null);
const KEY = "wiki-theme";

function initial(): Mode {
  const saved = localStorage.getItem(KEY);
  return saved === "light" || saved === "dark" ? saved : "dark";
}

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [mode, setMode] = useState<Mode>(initial);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", mode === "dark");
    localStorage.setItem(KEY, mode);
  }, [mode]);

  const toggle = () => setMode((m) => (m === "dark" ? "light" : "dark"));
  return <Ctx.Provider value={{ mode, toggle }}>{children}</Ctx.Provider>;
}

export function useTheme(): ThemeCtx {
  const c = useContext(Ctx);
  if (!c) throw new Error("useTheme fora do ThemeProvider");
  return c;
}
