"use client";

import { Form, TextField, ButtonGroup, Button } from "@adobe/react-spectrum";
import { useState } from "react";

const CustomForm = () => {
  const [name, setName] = useState("");

  const onSubmit: (event: React.FormEvent<HTMLFormElement>) => void = (e) => {
    e.preventDefault();
    console.log(`name=${name}`);
  };

  return (
    <Form validationBehavior="native" onSubmit={onSubmit} maxWidth="size-3000">
      <TextField label="Name" value={name} onChange={setName} isRequired />
      <div>You entered: {name}</div>
      <ButtonGroup>
        <Button type="submit" variant="accent">
          Submit
        </Button>
        <Button type="reset" variant="secondary">
          Reset
        </Button>
      </ButtonGroup>
    </Form>
  );
};

export default CustomForm;
