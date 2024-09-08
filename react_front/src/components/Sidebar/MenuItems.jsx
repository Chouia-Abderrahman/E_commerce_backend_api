// src/components/Sidebar/MenuItems.jsx
import { VStack, Icon, Text } from "@chakra-ui/react";
import { FaChartPie, FaShoppingCart, FaTags, FaUser, FaLayerGroup } from "react-icons/fa";

function MenuItems() {
  const menuItems = [
    { name: "Dashboard", icon: FaChartPie },
    { name: "Ecommerce", icon: FaShoppingCart },
    { name: "Category", icon: FaTags },
    { name: "Users", icon: FaUser },
    { name: "Roles", icon: FaLayerGroup },
  ];

  return (
    <VStack align="start" spacing={4}>
      {menuItems.map((item, index) => (
        <VStack key={index} align="start" spacing={1}>
          <Icon as={item.icon} boxSize={5} color="gray.600" />
          <Text>{item.name}</Text>
        </VStack>
      ))}
    </VStack>
  );
}

export default MenuItems;
