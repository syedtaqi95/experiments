import { McpServer } from "@modelcontextprotocol/server";
import { serveStdio } from "@modelcontextprotocol/server/stdio";
import * as z from "zod/v4";

function createServer(): McpServer {
  const server = new McpServer({
    name: "bmi-server",
    version: "1.0.0",
  });

  server.registerTool(
    "calculate_bmi",
    {
      description:
        "Calculate body mass index from a person's weight and height.",

      inputSchema: z.object({
        weightKg: z
          .number()
          .positive()
          .multipleOf(0.01)
          .describe("Weight in kilograms"),

        heightM: z
          .number()
          .positive()
          .multipleOf(0.01)
          .describe("Height in metres"),
      }),
    },

    async ({ weightKg, heightM }) => {
      const bmi = weightKg / heightM ** 2;
      const roundedBmi = Math.round(bmi * 10) / 10;

      return {
        content: [
          {
            type: "text",
            text: `The calculated BMI is ${roundedBmi}.`,
          },
        ],

        structuredContent: {
          bmi: roundedBmi,
          weightKg,
          heightM,
        },
      };
    },
  );

  server.registerTool(
    "convert_height",
    {
      description: "Convert a height in feet and inches to metres",

      inputSchema: z.object({
        feet: z.number().int().nonnegative(),
        inches: z.number().min(0).max(11),
      }),
    },

    async ({ feet, inches }) => {
      const totalInches = feet * 12 + inches;
      const metres = totalInches * 0.0254;
      const roundedMetres = Math.round(metres * 1000) / 1000;

      return {
        content: [
          {
            type: "text",
            text: `${feet} ft ${inches} in is ${roundedMetres} metres.`,
          },
        ],

        structuredContent: {
          feet,
          inches,
          metres: roundedMetres,
        },
      };
    },
  );

  return server;
}

void serveStdio(createServer);

console.error("BMI MCP server is running over stdio");
