"use client";

import { defaultTheme, Provider } from "@adobe/react-spectrum";
import type { ReactNode } from "react";

export const App = ({ children }: { children: ReactNode }) => {
  return (
    <Provider theme={defaultTheme} colorScheme="dark">
      {children}
    </Provider>
  );
};
