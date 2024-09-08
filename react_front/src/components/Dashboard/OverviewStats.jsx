// src/components/Dashboard/OverviewStats.jsx
import { SimpleGrid, Stat, StatLabel, StatNumber, Box } from "@chakra-ui/react";

function OverviewStats() {
  return (
    <SimpleGrid columns={{ base: 1, md: 3 }} spacing={6} mb={6}>
      <StatBox label="Total Sales" value="34,945" percentage={1.56} />
      <StatBox label="Total Income" value="$37,802" percentage={-1.56} />
      <StatBox label="Total Visitors" value="34,945" percentage={1.56} />
    </SimpleGrid>
  );
}

function StatBox({ label, value, percentage }) {
  return (
    <Box p={4} bg="white" borderRadius="md" shadow="sm">
      <Stat>
        <StatLabel>{label}</StatLabel>
        <StatNumber>{value}</StatNumber>
      </Stat>
    </Box>
  );
}

export default OverviewStats;
