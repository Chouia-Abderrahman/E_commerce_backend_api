// src/pages/Dashboard.jsx
import { Box, SimpleGrid, Stat, StatLabel, StatNumber } from "@chakra-ui/react";
import RecentOrders from "../components/Dashboard/RecentOrders";
import OverviewStats from "../components/Dashboard/OverviewStats";

function Dashboard() {
  return (
    <Box p={6} mt="64px">
      <OverviewStats />
      <RecentOrders />
    </Box>
  );
}

export default Dashboard;
