module.exports = {
  stories: ["../src/**/*.stories.mdx", "../src/**/*.stories.@(js|jsx|ts|tsx)"],
  refs: {
    "design-system": {
      title: "My design system",
      //👇 The url provided by Chromatic when it was deployed
      url: "https://641c3cdf0809fb9091120576-wditvaisdj.chromatic.com/",
    },
  },
  staticDirs: ["../public"],
  addons: [
    "@storybook/addon-links",
    "@storybook/addon-essentials",
    "@storybook/preset-create-react-app",
    "@storybook/addon-interactions",
  ],
  framework: "@storybook/react",
};
