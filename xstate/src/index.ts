import { assign, createActor, setup } from "xstate";

function main(): void {
  const toggleMachine = setup({
    types: {
      context: {} as { count: number; maxCount: number },
      input: {} as { maxCount: number },
    },
  }).createMachine({
    id: "toggle",
    context: ({ input }) => ({
      count: 0,
      maxCount: input.maxCount,
    }),
    initial: "Inactive",
    states: {
      Inactive: {
        on: {
          toggle: {
            guard: ({ context }) => context.count < context.maxCount,
            target: "Active",
          },
        },
      },
      Active: {
        entry: assign({
          count: ({ context }) => context.count + 1,
        }),
        on: { toggle: "Inactive" },
        after: { 2000: "Inactive" },
      },
    },
  });

  // Create actor that you can send events to
  const actor = createActor(toggleMachine, { input: { maxCount: 10 } });

  // Subscribe to snapshots (emitted state changes) from the actor
  actor.subscribe((snapshot) => {
    console.log(`Value: ${snapshot.value}`);
  });

  // Start the actor
  actor.start();
  console.log("Started actor");

  // Send events
  actor.send({ type: "toggle" }); // Logs Active
  actor.send({ type: "toggle" }); // Logs Inactive
}

main();
