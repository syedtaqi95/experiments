async function main() {
  // Create a new application
  const app = new PIXI.Application();
  await app.init({ width: 640, height: 360 });

  // Add canvas to HTML
  document.body.appendChild(app.canvas);

  // Add sprite to canvas
  await PIXI.Assets.load("sample.png");
  let sprite = PIXI.Sprite.from("sample.png");
  app.stage.addChild(sprite);

  // Create update loop and update sprite's X position over time
  let elapsed = 0.0;
  app.ticker.add((ticker) => {
    elapsed += ticker.deltaTime;
    sprite.x = 100.0 + Math.cos(elapsed / 50.0) * 100.0;
  });
}

await main();
