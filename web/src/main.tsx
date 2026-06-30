import "@fontsource-variable/inter";
import "@fontsource-variable/playfair-display";
import "@fontsource-variable/nunito-sans";
import "@fontsource/lora/500.css";
import "@fontsource/lora/500-italic.css";
import "./theme.css";

import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { App } from "./App";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>
);
