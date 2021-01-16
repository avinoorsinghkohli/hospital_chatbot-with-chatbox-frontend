## query+number
* greet
  - utter_greet
* search_patient_record
  - utter_number
* patient_imr
  - action_patient_record
* thanks
  - utter_goodbye

## testing+resp
* greet
  - utter_greet
* testing
  - utter_upload
* resp
  - utter_positive
* thanks
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story

* greet
    - utter_greet
* search_patient_record
    - utter_number
* patient_imr{"number":"1"}
    - action_patient_record
* thanks
    - utter_goodbye
