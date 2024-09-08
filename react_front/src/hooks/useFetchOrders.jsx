// src/hooks/useFetchOrders.js
import { useEffect, useState } from "react";
import axios from "axios";

const useFetchOrders = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    axios
      .get("/api/orders")
      .then((response) => {
        setOrders(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return orders;
};

export default useFetchOrders;
