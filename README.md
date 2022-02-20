## firebase-crud
_Best Python package to perform CRUD operations with firebase out there._

With firebase-crud, you can used to perform all kind of CRUD operations against firebase node with simple key value based (or) NoSQL based structure for the realtime usage.

# Installation

`pip install firebase-crud`

# Usage
firebase crud was programmed in ease-of-use in mind. It can simply import using below

`from firebase_crud import Collection`

# Prequisites
- Create and configure firebase console application.
- Generate API/SDK Key on Settings > Service Accounts > Python
- Configure realtime database path.

Once you have done with this configuration, you can easily initiate firebase using this package. But you have to prepare some things for the initialization.

- API Key - Path for the generated JSON file from firebase.
- Firebase URL - This url can be found in realtime database page on your firebase console.
- Collection Name - Usually single firebase project can have multiple collection/nodes. so you have to specify name for each collection.
- Unique Id - Firebase will generate some random unique key and which we cannot use to perform CRUD operations. So we need to init with some key as unique.

# Initialization

`sample_collection = Collection(api_key, path, 'ToDo', 'id')`

# Methods

Here you can find the list of methods available in this package.


Name | Description | Input | Output 
--- | --- | --- | --- 
`insert(value)` | To add/insert new items into collection | dict: `{'id':1, 'task':'Task'}` | `Boolean` | 
`getAllValues()` | To get all the items as list | None | `list` | 
`GetValue()` | To get the item by unique value | id: 1 | `dict` or `None` | 
`deleteAll()` | To delete all the items in the collection | None | `Boolean` | 
`update(self, unique_key, value)` | To update an item in the collection | unique_key: 1, dict: `{'id':1, 'task':'Task'}` | `Boolean` | 
`delete(unique_key)` | To delete an item from the collection | unique_key: 1 | `Boolean` | 

## Development

Want to contribute? Great!

Create pull request from the [github repository](https://github.com/jeganathpv/firebase-crud) and assign it to me.

## License

MIT License

Copyright (c) 2022 Jeganath PV

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


**Free Software, Hell Yeah!**

