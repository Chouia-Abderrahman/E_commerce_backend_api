// src/pages/Dashboard.jsx
import { Box } from "@chakra-ui/react";
import OverviewStats from "../components/Dashboard/OverviewStats";
import RecentOrders from "../components/Dashboard/RecentOrders";

function Dashboard() {
  return (
    <Box p={6} mt="64px"> {/* Ensure proper padding */}
      <OverviewStats />
      <RecentOrders />
    </Box>
  );
}

export default Dashboard;
