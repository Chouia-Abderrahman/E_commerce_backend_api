// src/components/Dashboard/Pagination.jsx
import { Flex, Button } from "@chakra-ui/react";

function Pagination() {
  return (
    <Flex justify="center" mt={4}>
      <Button variant="ghost">1</Button>
      <Button variant="solid">2</Button>
      <Button variant="ghost">3</Button>
    </Flex>
  );
}

export default Pagination;
