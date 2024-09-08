// src/components/Sidebar/Sidebar.jsx
import { Box, VStack } from "@chakra-ui/react";
import MenuItems from "./MenuItems";

function Sidebar() {
  return (
    <Box
      w="250px"
      bg="white"
      boxShadow="md"
      position="fixed"
      height="100vh"
      p={4}
    >
      <VStack align="start" spacing={4}>
        <MenuItems />
      </VStack>
    </Box>
  );
}

export default Sidebar;
