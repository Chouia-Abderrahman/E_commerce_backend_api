// src/App.jsx
import { Box, Flex } from "@chakra-ui/react";
import Sidebar from "./components/Sidebar/Sidebar";
import Header from "./components/Header/Header";
import Dashboard from "./pages/Dashboard";
import { ChakraProvider } from "@chakra-ui/react";

function App() {
  return (

    <Flex height="100vh">
      <Sidebar />
      <Box flex="1" bg="#f4f4f9"> {/* Ensure background is applied */}
        <Header />
        <Dashboard />
      </Box>
    </Flex>
    
  );
}

export default App;
