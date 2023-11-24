"use client";

import { useState } from "react";
import {
  Button,
  FieldError,
  Form,
  Input,
  Label,
  TextField,
} from "react-aria-components";

const CustomForm = () => {
  const [name, setName] = useState("");
  const [isInvalid, setInvalid] = useState(false);
  const isRequired = true;

  const onSubmit: (event: React.FormEvent<HTMLFormElement>) => void = (e) => {
    e.preventDefault();
    console.log(`name=${name}`);
    setInvalid(false);
  };

  const onInvalid: (event: React.FormEvent<HTMLFormElement>) => void = (e) => {
    e.preventDefault();
    setInvalid(true);
  };

  const onReset: (event: React.FormEvent<HTMLFormElement>) => void = (e) => {
    setName("");
    setInvalid(false);
  };

  return (
    <Form
      onSubmit={onSubmit}
      onInvalid={onInvalid}
      onReset={onReset}
      className="max-w-[240px]"
    >
      <TextField
        name="Name"
        value={name}
        onChange={setName}
        isRequired={isRequired}
        className="gap mt-2 flex flex-col"
      >
        <Label className="pb-[5px] pt-[4px] text-xs text-neutral-300">
          Custom-Name {isRequired && <span>*</span>}
        </Label>

        <Input className="w-full rounded border border-neutral-500 bg-black px-3 py-1 transition hover:border-neutral-400 focus:border-blue-500 focus:outline-none" />

        <FieldError className="py-1 text-xs text-red-400" />
      </TextField>

      <div className="mt-2">You entered: {name}</div>

      <div className="mt-2 flex flex-row gap-4">
        <Button
          type="submit"
          className="rounded-2xl border-2 border-red-600 bg-red-600 px-[14px] py-1 font-bold transition hover:border-red-700 hover:bg-red-700"
        >
          Submit
        </Button>

        <Button
          type="reset"
          className="rounded-2xl border-2 border-neutral-600 bg-none px-[14px] py-1 font-bold transition hover:border-neutral-500 hover:bg-neutral-700"
        >
          Reset
        </Button>
      </div>
    </Form>
  );
};

export default CustomForm;
