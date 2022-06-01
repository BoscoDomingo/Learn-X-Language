# SwiftUI

Views are now value types, coming from `struct`, and are a function/result of their state, no longer do you have to manually update each one of them.

SwiftUI views must have a `ContentView` which in itself has a `body`, which is what is rendered, and *modifiers* for the different elements in that body. Ultimately, small atomic blocks make up greater architectures.

```Swift
struct ContentView: View {
    var body: some View {
        Text("Hello World")
    }
}
```

The order of modifiers affects the final result, so be careful. For example:

```Swift
Text("Some text").background(Color.blue).padding() //The padding is NOT coloured
Text("Some text").padding().background(Color.blue) //The padding is coloured
```

And it is important to not that a modifier will be applied to an entire View if applicable. If not, it will trickle down into its inside Views. For example:

```Swift
var body: some View{
    ZStack{
        ...
    }.padding() //applies to whole ZStack
    .foregroundColor(.black) //applies to views inside ZStack
}
```

## Cycle of interactions

![Cycle of interactions](https://i.imgur.com/RDykMxL.png)

## States and bindings

You should **only have 1 source of truth** for each piece of information (either 1 `@State` or `BindableObject` per property), meaning all other Views that want to use that source of truth should make use of `@Binding`s (Bindings are read-write). `@State` is not a great fit for external data (such as things coming from backend), since it is "stuck" inside SwiftUI. Use the `BindableObject` protocol for these types of data:

<img width="700" alt="Single Source of Truth" src="https://user-images.githubusercontent.com/46006784/111323064-d5b48e00-8669-11eb-89cf-5ed564fc46ab.png">

![@State and BindableObject](https://user-images.githubusercontent.com/46006784/111322732-840c0380-8669-11eb-8f0d-281f5f746af3.png)

![@Binding](https://i.imgur.com/0LPvONN.png)

`@State` means *"this is a property that's gonna change as the program runs"*, and SwiftUI takes care of memory management **and** watching the value.

With the `$` prefix, SwiftUI creates a two-way binding, meaning any updates through external actions (user interaction, Publishers) will be reflected back to the original property.

Generally speaking, you want to avoid the use of `@State` and favour other alternatives when possible.

## Information from a Model

`@ObjectBinding` is akin to `@State` except it works between a Model and a View that listens to said Model's property's changes, where `@State` is between Views themselves, and won't work with classes. This means that classes you use must conform to the `BindableObject` protocol, and implement `didChange()`.

![@ObjectBinding](https://i.imgur.com/K80oZAb.png)
An alternative for hierarchies is `@EnvironmentObject` which avoids having to pass the `BindableObject` property from View to View, and instead grab it straight from `Environment`, always with 1 source of truth and thus no concurrency problems.
![@EnvironmentObject](https://i.imgur.com/kgut0rm.png)
![Screenshot 2021-03-16 at 15 00 21](https://user-images.githubusercontent.com/46006784/111322877-ab62d080-8669-11eb-9219-a3da230e8668.png)
<img width="900" src="https://user-images.githubusercontent.com/46006784/111327975-2332fa00-866e-11eb-9e20-8e92346c82d5.png">

## Go-to article

Wonderful article explaining all the aforementioned property wrappers **in detail**, including when to use which and code examples: [Jared Sinclair Blog](https://jaredsinclair.com/2020/05/07/swiftui-cheat-sheet.html)

## Hosting SwiftUI inside UIKit

- `UIHostingController` - For iOS apps
- `NSHostingController` - For MacOS apps
- `WKHostingController` - For watchOS apps

They are all subclases of `UIViewController` and thus will work seamlessly with existing UIKit views.

```Swift
let hostingController = UIHostingController(rootView: SomeSwiftUIView)
```

![Screenshot 2021-03-16 at 15 12 23](https://user-images.githubusercontent.com/46006784/111323487-36dc6180-866a-11eb-8c9b-0304c3348068.png)

## Hosting UIKit inside SwiftUI

The `Representable` protocol exists for this purpose.

- `UIViewRepresentable` - For iOS apps
- `NSViewRepresentable` - For MacOS apps
- `WKInterfaceObjectRepresentable` - For watchOS apps

<img width="900" src="https://user-images.githubusercontent.com/46006784/111323872-8ae74600-866a-11eb-84e3-c32f9a2e5822.png">

### View Lifecycle inside SwiftUI

<img width="900" src="https://user-images.githubusercontent.com/46006784/111326815-27aae300-866d-11eb-922f-225299630d84.png">

## Know more/Code snippets

* [A great resource for some example code with image previews](https://github.com/fzhlee/SwiftUI-Guide/blob/master/README_English.md)
* [Everything you'll ever need about SwiftUI](https://github.com/Juanpe/About-SwiftUI/blob/master/README.md)
