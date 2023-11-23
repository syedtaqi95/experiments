'use client'

import { defaultTheme, Provider } from "@adobe/react-spectrum"
import type { ReactNode } from "react"

export const App = ({ children }: { children: ReactNode }): JSX.Element => {
  return (
    <Provider theme={defaultTheme}>
      {children}
    </Provider>
  )
}
