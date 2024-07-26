using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;

namespace NorthwindApp
{
    public class DataAccessLayer
    {
        private readonly string _connectionString;

        public DataAccessLayer(string connectionString)
        {
            _connectionString = connectionString;
        }

        public int GetCustomerCount()
        {
            using (SqlConnection connection = new SqlConnection(_connectionString))
            {
                connection.Open();
                SqlCommand command = new SqlCommand("SELECT COUNT(*) FROM Customers", connection);
                return (int)command.ExecuteScalar();
            }
        }

        public List<string> GetCustomerLastNames()
        {
            List<string> lastNames = new List<string>();
            using (SqlConnection connection = new SqlConnection(_connectionString))
            {
                connection.Open();
                SqlCommand command = new SqlCommand("SELECT LastName FROM Customers", connection);
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        lastNames.Add(reader["LastName"].ToString());
                    }
                }
            }
            return lastNames;
        }
    }
}
