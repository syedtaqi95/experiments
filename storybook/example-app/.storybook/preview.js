import React from "react";

// The styles imported from the design system.
import { global as designSystemGlobal } from "@syedtaqi95/learnstorybook-design-system";

const { GlobalStyle } = designSystemGlobal;

/*
 * Adds a global decorator to include the imported styles from the design system.
 * More on Storybook decorators at:
 * https://storybook.js.org/docs/react/writing-stories/decorators#global-decorators
 */
export const decorators = [
  (Story) => (
    <>
      <GlobalStyle />
      <Story />
    </>
  ),
];
/*
 * More on Storybook parameters at:
 * https://storybook.js.org/docs/react/writing-stories/parameters#global-parameters
 */
export const parameters = {
  actions: { argTypesRegex: "^on[A-Z].*" },
};
