import React from 'react';
import { getHelloWorld } from '@org/scope-name.get-hello-world';

export function HelloWorld() {
  return <div>{getHelloWorld()}</div>;
}
