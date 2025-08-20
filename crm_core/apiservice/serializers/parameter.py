from rest_framework import serializers


class AirlineParameterSerializer(serializers.Serializer):
    source_iata = serializers.CharField(error_messages={
        'required': 'sourceIata value can not be null', 
        'blank': 'sourceIata value can not be null', 
        'null': 'sourceIata value can not be null'})
    destination_iata = serializers.CharField(error_messages={
        'required': 'destinationIata value can not be null', 
        'blank': 'destinationIata value can not be null', 
        'null': 'destinationIata value can not be null'})
    departure_date = serializers.DateField(error_messages={
        'required': 'departuredate value can not be null', 
        'blank': 'departuredate value can not be null', 
        'null': 'departuredate value can not be null'})
    

class HotelParameterSerializer(serializers.Serializer):
    hotel_id = serializers.CharField(error_messages={
        'required': 'hotel_id value can not be null', 
        'blank': 'hotel_id value can not be null', 
        'null': 'hotel_id value can not be null'})
    checkIn_date = serializers.DateField(error_messages={
        'required': 'checkIn_date value can not be null', 
        'blank': 'checkIn_date value can not be null', 
        'null': 'checkIn_date value can not be null'})
    number_of_stay = serializers.IntegerField(min_value=1, error_messages={
        'required': 'numberOfStay value can not be null', 
        'blank': 'numberOfStay value can not be null', 
        'null': 'numberOfStay value can not be null'})

