// Resource declaration basic template
/*
resource <symbolic name> ‘Microsoft.<resource type>@<api version>’ = {
  // Required properties
  name: ‘<resource name>’
  location: ‘<Azure region>’
  // Remaining resource-specific properties
  // ...
  }

  // The symbolic name is only for internal reference within the file
*/

// Complete Bicep template
/*
// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/file
targetScope = '<scope>'

@<decorator>(<argument>)
param <parameter-name> <parameter-data-type> = <default-value>

var <variable-name> = <variable-value>

resource <resource-symbolic-name> '<resource-type>@<api-version>' = {
  <resource-properties>
}

module <module-symbolic-name> '<path-to-file>' = {
  name: '<linked-deployment-name>'
  params: {
    <parameter-names-and-values>
  }
}

output <output-name> <output-data-type> = <output-value>
*/

// Target Scope
/* A special variable is the `targetScope`, which defaults to `resourceGroup`. Defines the level at which the deployment will take place and therefore
the allowed actions.
*/
targetScope = 'resourceGroup'

// Parameters and variables
/*
Parameters vary across deployments, and are specific to each one.
Variables hold values that will change during the deployment, but said evolution can be the same across all deployments.

When you declare parameters, you must pass a value to the Bicep template during deployment
Parameter files in JSON can also be employed.
*/
@minLength(3)
@maxLength(24) // Decorators can be used to add additional constraints to parameters
@description('The name of the resource') // Or even useful information
param name string // Will need to be specified when deploying this template
param location string = resourceGroup().location // Optional parameter, defaults to the resource group's location
var stgAcctName = concat(name, '2468') // Variables don't need a specific type, but do require a value

@allowed([
  'dev'
  'prod'
])
param environment string = 'dev'
var isProd = environment == 'prod'

// Expressions and Functions
param someUniqueString string = uniqueString(resourceGroup().id) // uniqueString takes a seed, in this case the RG's id

// String interpolation - ${}
var stgAcctNameInterpolated = '${name}${someUniqueString}'

// Conditional operators
var skuName = environment == 'prod' ? 'Premium_LRS' : 'Standard_LRS'

resource stgAcct 'Microsoft.Storage/storageAccounts@2021-02-01' = {
  name: stgAcctNameInterpolated
  location: location
  kind: 'StorageV2'
  sku: {
    name: skuName
  }
}

// Loops/Iteration & Collections
param storageCount int = 2

// For loops
/* A for loop can be used to create multiple resources of the same type in sequence */
resource createStorages 'Microsoft.Storage/storageAccounts@2021-06-01' = [for i in range(0, storageCount): {
  name: '${i}storage${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: skuName
  }
  kind: 'StorageV2'
}]

/* They also work on outputs */
output names array = [for i in range(0, storageCount): {
  name: createStorages[i].name
}]

// Arrays
/* You can also loop through arrays (note the lack of comas between objects) */
param storages array = [
  {
    name: 'contoso'
    skuName: 'Standard_LRS'
  }
  {
    name: 'fabrikam'
    skuName: 'Premium_LRS'
  }
]

/* Since this array's elements are objects, you can use dot notation to access the properties */
resource createStoragesFromArray 'Microsoft.Storage/storageAccounts@2021-06-01' = [for storage in storages: {
  name: '${storage.name}obj${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: storage.skuName
  }
  kind: 'StorageV2'
}]

param storageNames array = [
  'contoso'
  'fabrikam'
]

/* You can also iterate through an array and grab the indeces as you go! */
resource createStoragesFromArrayWIthIndex 'Microsoft.Storage/storageAccounts@2021-06-01' = [for (name, i) in storageNames: {
  name: '${i}${name}${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: name == 'contoso' ? 'Standard_LRS' : 'Premium_LRS'
  }
  kind: 'StorageV2'
}]

/* And even loop over arrays inside a parent resource */
param vNetInfo object = {
  'name': 'vnet-onpremises'
  'range': '10.0.0.0/24'
  'subnets': [
    {
      'name': 'NetworkVirtualAppliances'
      'range': '10.0.0.0/28'
    }
    {
      'name': 'GatewaySubnet'
      'range': '10.0.0.240/28'
    }
  ]
}

resource VNetOnPrem 'Microsoft.Network/virtualNetworks@2021-05-01' = {
  name: vNetInfo.name
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        vNetInfo.range
      ]
    }
    subnets: [for subnet in vNetInfo.subnets: { // Here
      name: subnet.name
      properties: {
        addressPrefix: subnet.range
      }
    }]
  }
}

// Dictionaries
/* Dictionaries require at least the use of the items() function */
param storageConfig object = {
  storage1: {
    name: 'contoso'
    skuName: 'Standard_LRS'
  }
  storage2: {
    name: 'fabrikam'
    skuName: 'Premium_LRS'
  }
}

resource createStoragesWithDictionaries 'Microsoft.Storage/storageAccounts@2021-06-01' = [for config in items(storageConfig): {
  name: '${config.value.name}${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: config.value.skuName
  }
  kind: 'StorageV2'
}]

// Loop with condition
/* Using an `: if()` expression, you can loop through an array and only create resources when a condition is met */
resource createStoragesInDev 'Microsoft.Storage/storageAccounts@2021-06-01' = [for i in range(0, storageCount): if (!isProd) {
  name: '${i}storage${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}]

//Outputs
/* These outputs can be used for chaining modules. They will be available to the parent module in moduleName.outputs
NEVER output secrets. */
output someOutput string = stgAcctNameInterpolated // "someOutput" will be included in the output together with the value. They can share the same name, as well

// Modules
/* The way to keep complexity lower and reusability higher. Some good practices include:
A module should have a clear purpose.
Don't put every resource into its own module.
A module should have clear parameters and outputs that make sense.
A module should be as self-contained as possible.
 */
module createStoragesFromModule './createStorages.bicep' = {
  name: '${name}module'
  params: {
    name: '${name}module'
    location: location
    skuName: skuName
    kind: 'StorageV2'
  }
}

// Deployment
/* Deployment can be done by transpiling to JSON first, or using the Bicep template directly (in which case it is still transpiled to JSON under the hood) */

// Direct deployment:
// Azure CLI for a Resource Group
/*
az deployment group create \
--resource-group bicep_RG \
--template-file Learning_bicep.bicep \
--parameters name='stgacctbicepazcli'
*/

//Azure CLI for a subscription
/*
az deployment sub create \
-l westeurope \
-n some_deployment \
--template-file /path/to/teplate.bicep \
--parameters /path/to/parameters.json
*/

// PowerShell
/*
New-AzResourceGroupDeployment `
-ResourceGroupName bicep_RG `
-TemplateFile Learning_bicep.bicep `
-nameFromTemplate 'stgacctbicepdemo' // This is necessary since the command already has a parameter called name
 */


// Transpilation:
// bicep build Learning_bicep.bicep <-- Generates a JSON
// bicep decompile Learning_bicep.json <-- Generates a Bicep template (not guaranteed to work)

// Notes:
/* Bicep is strict with newlines/line breaks, so be aware */
