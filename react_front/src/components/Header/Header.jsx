// src/components/Header/Header.jsx
import { Flex, IconButton, Input, Spacer, Avatar, Box } from "@chakra-ui/react";
import { FaBell, FaCog, FaSearch } from "react-icons/fa";

function Header() {
  return (
    <Flex p={4} align="center" boxShadow="md" bg="white">
      <Box>
        <Input placeholder="Search..." w="400px" />
      </Box>
      <Spacer />
      <IconButton icon={<FaSearch />} variant="ghost" aria-label="Search" />
      <IconButton icon={<FaBell />} variant="ghost" aria-label="Notifications" />
      <IconButton icon={<FaCog />} variant="ghost" aria-label="Settings" />
      <Avatar name="Kristin Watson" src="https://bit.ly/broken-link" />
    </Flex>
  );
}

export default Header;
