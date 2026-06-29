import { useTheme } from "../lib/theme";

export function ThemeToggle() {
  const { mode, toggle } = useTheme();
  return (
    <button
      onClick={toggle}
      title="Alternar tema claro/escuro"
      className="grid size-9 place-items-center rounded-lg border border-border text-base
                 transition-colors hover:bg-muted"
    >
      {mode === "dark" ? "☀️" : "🌙"}
    </button>
  );
}
