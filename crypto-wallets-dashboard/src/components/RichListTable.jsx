import React from 'react';

import { Table } from 'antd';

const RichListTable = ({ richList }) => {

    const columns = [
        {
            title: 'Address',
            dataIndex: 'addr',
            key: 'address',
        },
        {
            title: 'Balance',
            dataIndex: 'balance',
            key: 'balance',
            defaultSortOrder: 'descend',
            sorter: (a, b) => a.balance - b.balance,
        }
    ];

    return (
        <Table dataSource={ richList } columns={ columns } />
    )
}

export default RichListTable;
