using System.Collections.Generic;

namespace NorthwindApp
{
    public class BusinessLayer
    {
        private readonly DataAccessLayer _dataAccessLayer;

        public BusinessLayer(string connectionString)
        {
            _dataAccessLayer = new DataAccessLayer(connectionString);
        }

        public int GetNumberOfCustomers()
        {
            return _dataAccessLayer.GetCustomerCount();
        }

        public List<string> GetCustomerLastNames()
        {
            return _dataAccessLayer.GetCustomerLastNames();
        }
    }
}
