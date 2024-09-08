// src/components/Sidebar/Sidebar.jsx
import { Box, VStack, Flex } from "@chakra-ui/react";
import MenuItems from "./MenuItems";

function Sidebar() {
  return (
    <Flex
    align="start"
    zIndex={99}
    
    >
    <Box
      bg="white"
      boxShadow="md"
      position="fixed"
      height="100vh"
      padding={4}
      width={200}
      
    >
      <div>
        <MenuItems />
      </div>
    </Box>
    </Flex>
  );
}

export default Sidebar;
