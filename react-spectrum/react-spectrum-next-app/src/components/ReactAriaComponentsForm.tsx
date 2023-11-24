"use client";

import { useState } from "react";

const CustomForm = () => {
  const [name, setName] = useState("");

  const onSubmit: (event: React.FormEvent<HTMLFormElement>) => void = (e) => {
    e.preventDefault();

    console.log(`name=${name}`);
  };

  return <>Placeholder</>;
};

export default CustomForm;
