"use client";

import { cn } from "@/utils/cn";
import type { ComponentPropsWithRef, FC } from "react";
import { useState } from "react";
import {
  Button as BaseButton,
  FieldError,
  Form,
  Input,
  Label,
  TextField,
} from "react-aria-components";

const Button: FC<ComponentPropsWithRef<typeof BaseButton>> = (props) => {
  const { className, ...otherProps } = props;
  return (
    <BaseButton
      {...otherProps}
      className={cn(
        "cursor-default rounded-2xl border-2 px-[14px] py-1 font-bold outline-none transition",
        className,
      )}
    />
  );
};

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
    setInvalid(true);
  };

  const onReset: (event: React.FormEvent<HTMLFormElement>) => void = (e) => {
    setName("");
    setInvalid(false);
  };

  const onChange: (value: string) => void = (value) => {
    setName(value);
    setInvalid(value ? false : true);
  };

  const inputBorder = isInvalid
    ? "border-red-400 hover:border-red-300"
    : "border-neutral-500 hover:border-neutral-400";

  return (
    <Form
      onSubmit={onSubmit}
      onInvalid={onInvalid}
      onReset={onReset}
      className="max-w-[240px]"
    >
      <TextField
        name="Name"
        type="text"
        value={name}
        onChange={onChange}
        isRequired={isRequired}
        className="gap mt-2 flex flex-col"
      >
        <Label className="pb-[5px] pt-[4px] text-xs text-neutral-300">
          Custom-Name {isRequired && "* "}
        </Label>

        <Input
          className={`w-full rounded border bg-black px-3 py-1 transition  focus:border-blue-500 focus:outline-none ${inputBorder}`}
        />

        <FieldError className="py-1 text-xs text-red-400" />
      </TextField>

      <div className="mt-2">You entered: {name}</div>

      <div className="mt-2 flex flex-row gap-4">
        <Button
          type="submit"
          className="border-red-600 bg-red-600 hover:border-red-700 hover:bg-red-700 pressed:border-red-800 pressed:bg-red-800"
        >
          Submit
        </Button>

        <Button
          type="reset"
          className="border-neutral-600 bg-transparent  hover:border-neutral-500 hover:bg-neutral-700 pressed:border-neutral-400 pressed:bg-neutral-600"
        >
          Reset
        </Button>
      </div>
    </Form>
  );
};

export default CustomForm;
