import { Moon, Sun } from "lucide-react";
import { useTheme } from "../lib/theme";

export function ThemeToggle() {
  const { mode, toggle } = useTheme();
  return (
    <button
      type="button"
      onClick={toggle}
      title="Alternar tema claro/escuro"
      className="group inline-flex h-10 w-10 items-center justify-center rounded-full
                 border border-border/60 bg-card/60 text-foreground/60 transition
                 hover:border-primary/40 hover:text-primary"
    >
      {mode === "dark" ? (
        <Sun className="h-[18px] w-[18px] transition-transform duration-300 group-hover:rotate-45" strokeWidth={1.5} />
      ) : (
        <Moon className="h-[18px] w-[18px] transition-transform duration-300 group-hover:-rotate-12" strokeWidth={1.5} />
      )}
    </button>
  );
}
