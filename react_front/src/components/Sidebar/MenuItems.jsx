// src/components/Sidebar/MenuItems.jsx
import { VStack, Icon, Text, Flex, Box } from "@chakra-ui/react";
import {
  FaChartPie,
  FaShoppingCart,
  FaTags,
  FaUser,
  FaLayerGroup,
} from "react-icons/fa";

function MenuItems() {
  const menuItems = [
    { name: "Dashboard", icon: FaChartPie },
    { name: "Ecommerce", icon: FaShoppingCart },
    { name: "Category", icon: FaTags },
    { name: "Users", icon: FaUser },
    { name: "Roles", icon: FaLayerGroup },
  ];

  return (
    <div>
      {menuItems.map((item, index) => (
        <Flex key={index} gap="4" align={"start"} marginBottom={3}>
          <Box>
            <Icon as={item.icon} boxSize={5} color="gray.600" />
          </Box>
          <Box>
            <Text>{item.name}</Text>
          </Box>
        </Flex>
      ))}
    </div>
  );
}

export default MenuItems;
