"use client";

import { Button } from "@adobe/react-spectrum";
import React from "react";

const CustomForm = () => {
  return (
    <div>
      <Button
        variant="accent"
        onPress={() => {
          console.log("clicked");
        }}
      >
        Save
      </Button>
    </div>
  );
};

export default CustomForm;
