async function main() {
  // Create a new application
  const app = new PIXI.Application();
  await app.init({ width: 640, height: 360 });

  // Add canvas to HTML
  document.body.appendChild(app.canvas);

  // Add container to center our sprite on the page
  const container = new PIXI.Container({
    x: app.screen.width / 2,
    y: app.screen.height / 2,
  });
  app.stage.addChild(container);

  // Add sprite to canvas
  await PIXI.Assets.load("sample.png");

  const sprites = [];
  let parent = container;
  for (let i = 0; i < 3; i++) {
    let wrapper = new PIXI.Container();
    let sprite = PIXI.Sprite.from("sample.png");
    sprite.anchor.set(0.5);
    wrapper.addChild(sprite);
    parent.addChild(wrapper);
    sprites.push(sprite);
    parent = wrapper;
  }

  // Create update loop and update sprite's X position over time
  let elapsed = 0.0;
  app.ticker.add((ticker) => {
    elapsed += ticker.deltaTime / 60;
    const amount = Math.sin(elapsed);
    const scale = 1.0 + 0.25 * amount;
    const alpha = 0.75 * 0.25 * amount;
    const angle = 40 * amount;
    const x = 75 * amount;
    for (let i = 0; i < sprites.length; i++) {
      const sprite = sprites[i];
      sprite.scale.set(scale);
      sprite.alpha = alpha;
      sprite.angle = angle;
      sprite.x = x;
    }
  });
}

await main();
