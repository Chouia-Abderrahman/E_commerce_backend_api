// src/components/Dashboard/RecentOrders.jsx
import { Box, Table, Thead, Tbody, Tr, Th, Td } from "@chakra-ui/react";
import Pagination from "./Pagination";

function RecentOrders() {
  const orders = [
    { product: "Product 1", customer: "2,672", quantity: "X1", price: "$28,672", status: "Delivered" },
    { product: "Product 2", customer: "2,672", quantity: "X2", price: "$28,672", status: "Delivered" },
    // Add more data as needed
  ];

  return (
    <Box bg="white" p={6} borderRadius="md" shadow="sm">
      <Table variant="simple">
        <Thead>
          <Tr>
            <Th>Product</Th>
            <Th>Customer</Th>
            <Th>Quantity</Th>
            <Th>Price</Th>
            <Th>Status</Th>
          </Tr>
        </Thead>
        <Tbody>
          {orders.map((order, index) => (
            <Tr key={index}>
              <Td>{order.product}</Td>
              <Td>{order.customer}</Td>
              <Td>{order.quantity}</Td>
              <Td>{order.price}</Td>
              <Td>{order.status}</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
      <Pagination />
    </Box>
  );
}

export default RecentOrders;
