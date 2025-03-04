# Export Data Enrichment in your app

>> Use the exportDataEnrichment api to get whole data enrichment report.

```dart
home_page.dart

void initState(){
  AnagogFlutter.instance
    .exportDataEnrichment()
    .then((snapshot) {
      //Process your data enrichment snapshot
    }
    .catchError((err) {
    print("Something went error: ${err.toString()}");
  });
}
```

>> You may add a list or requested metrics to get specific Data Enrichment 

```dart
home_page.dart

void initState(){
 Set<String> metrics = { "IsBookReader", "CurrentTimeZone"};

  AnagogFlutter.instance
    .exportDataEnrichment(requestedMetrics: metrics)
    .then((snapshot) {
      //Process your data enrichment snapshot Map<String, dynamic>
      //Typical response
      /* {
          "IsBookReader" : TRUE,
          "CurrentTimerZone" : "Asia/Tokyo"
         }
      */
    }
    .catchError((err) {
    print("Something went error: ${err.toString()}");
  });


}
```

# Get Best Moment Event in Your Flutter Code

```dart
//For recieveing BestMoment when the app is in foreground or minimized
main.dart
void main() async {
   AnagogFlutter.instance.obtainEventStream().listen((event) {
      print("application - onAnagogEvent $event");
      _handleJedaiEvent(event);
    });
     runApp(MyFlutterApp());
}

  void _handleJedaiEvent(Map<dynamic, dynamic> event) {
    print("_handleAnagogEvent: $event");
    var action = event[ACTION] as String;
    showAlertDialog(context, action, "${event[PAYLOAD] ??= ""}");
    switch (action) {
      case ON_CAMPAIGN_TRIGGERED:
        {
          break;
        }
      
      
      case ON_BEST_MOMENT:{
        //Hey! It's the best moment to engage with your user
        break;
      }
      
    }
  }

```

# Get Best Moment and Other Events in Background

Getting events in background is done using a top level handler function which should be register using our **registerHeadlessDispatcher** API. 

Follow the instructions below to set and register your headless callback in your Dart code.



>> Define your headless callback as a top level functions. 

```dart
anagog_headless_callback.dart
@pragma('vm:entry-point') 
Future<void> anagogHeadlessCallback(String action, Map<String, dynamic> payload) async {
 //Here you'le get Edge SDK events when app is terminated
... handle all Edge SDK background events 

  **if (action == ON_BEST_MOMENT) {**
    **print("[anagogHeadlessCallback] ON_BEST_MOMENT, Hey, now its the best time to engeage with your users");**
    
  **}**
}
```

>> Register your headless top level functions in ***main.dart***

```dart
//For receiveing Best Moment when the app is in background or terminated
main.dart
void main() async {
  await WidgetsFlutterBinding.ensureInitialized();
  //Register your background handler
  await AnagogFlutter.instance.registerHeadlessDispatcher(anagogHeadlessCallback)
  runApp(JedaiSampleApp());
}
```



For additional instructions regarding Flutter integration checkout our [full documentation](https://dash.readme.com/project/anagog/v3.0/refs/flutter-plugin-integration-quickstart-guide)